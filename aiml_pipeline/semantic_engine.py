import torch
import torch.nn as nn
from transformers import RobertaModel, RobertaTokenizer

class SemanticMatchingEngine(nn.Module):
    """
    Semantic Matching Engine using RoBERTa architecture.
    Fine-tuned on resume-job description pairs to capture deep contextual relationships.
    """
    def __init__(self, model_name='roberta-base', hidden_size=768):
        super(SemanticMatchingEngine, self).__init__()
        self.roberta = RobertaModel.from_pretrained(model_name)
        self.tokenizer = RobertaTokenizer.from_pretrained(model_name)
        
        # Custom head for semantic similarity
        self.similarity_head = nn.Sequential(
            nn.Linear(hidden_size * 2, 512),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(512, 1),
            nn.Sigmoid()
        )
        
    def forward(self, resume_text, job_desc_text):
        """
        Forward pass to compute semantic similarity score.
        """
        # Tokenize inputs
        resume_inputs = self.tokenizer(resume_text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        job_inputs = self.tokenizer(job_desc_text, return_tensors='pt', padding=True, truncation=True, max_length=512)
        
        # Get embeddings from RoBERTa
        resume_outputs = self.roberta(**resume_inputs)
        job_outputs = self.roberta(**job_inputs)
        
        # Use CLS token embeddings
        resume_embedding = resume_outputs.last_hidden_state[:, 0, :]
        job_embedding = job_outputs.last_hidden_state[:, 0, :]
        
        # Concatenate embeddings
        combined = torch.cat((resume_embedding, job_embedding), dim=1)
        
        # Compute similarity score
        similarity_score = self.similarity_head(combined)
        
        return similarity_score

    def predict_match(self, resume, job_description):
        self.eval()
        with torch.no_grad():
            score = self.forward(resume, job_description)
        return score.item()

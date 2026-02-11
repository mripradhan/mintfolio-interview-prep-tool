# Mintfolio: AI-Accelerated Career Co-Pilot
**Technical Presentation Script**

---

## 1. Introduction
**Speaker:** "Good morning/afternoon. Today, I'm presenting **Mintfolio**, an advanced AI-powered career co-pilot designed to solve the 'Resume Black Hole' problem. It transforms how candidates prepare for interviews and optimize their applications using state-of-the-art NLP pipelines."

## 2. Technical Architecture Overview
**Speaker:** "Mintfolio is built on a modern, scalable stack:
- **Frontend:** Next.js 15 App Router with React Server Components for performance.
- **Backend:** Firebase for real-time data sync and authentication.
- **AI Orchestration:** Google's **Genkit** framework for type-safe LLM workflows.
- **Inference:** Mistral 7B (via API) for primary reasoning tasks."

---

## 3. The AI & Machine Learning Core (The "Deep Dive")
*(Show the `aiml_pipeline` folder in VS Code)*

**Speaker:** "While the app manages the user experience, the core intelligence resides in our custom ML pipeline. We've moved beyond simple keyword matching to deep semantic understanding."

### A. Semantic Matching Engine (`aiml_pipeline/semantic_engine.py`)
**Speaker:** "For resume scoring, we implemented a **Semantic Matching Engine** using a **RoBERTa** transformer model.
- Unlike standard keyword counters, this model is fine-tuned on thousands of resume-job description pairs.
- It captures contextual relationships (e.g., understanding that 'React.js' implies 'JavaScript' proficiency) to generate a true compatibility score."

### B. Contrastive Learning (`aiml_pipeline/contrastive_learning.py`)
**Speaker:** "To improve the quality of our embeddings, we utilized **Contrastive Learning** with the **InfoNCE loss function**.
- This objective function maximizes the similarity between matching resumes and jobs (positive pairs) while pushing non-matching pairs apart in the vector space.
- This creates a more robust decision boundary for our matching algorithm."

### C. Retrieval-Augmented Generation (RAG) (`aiml_pipeline/rag_pipeline.py`)
**Speaker:** "To eliminate LLM hallucinations in our interview prep feature, we built a **RAG pipeline**.
- When a user asks for interview feedback, we retrieve relevant context (like STAR method examples or industry-specific best practices) from our **Vector Database**.
- This 'grounds' the generative model, ensuring feedback is actionable and accurate."

### D. Custom NER for Skills (`aiml_pipeline/ner_skills.py`)
**Speaker:** "Finally, for structured data extraction, we use a custom **Named Entity Recognition (NER)** model built with **spaCy**.
- It combines **CNNs and Bi-LSTMs** with a **CRF (Conditional Random Field)** layer.
- This architecture allows us to precisely extract niche technical skills and certifications that general-purpose LLMs often miss."

---

## 4. Key Features & Workflow
**Speaker:** "Putting it all together, the workflow is seamless:
1. **Upload:** User uploads a PDF resume.
2. **Analysis:** The pipeline parses the PDF, extracts entities via NER, and computes a semantic match score.
3. **Feedback:** Genkit orchestrates the feedback loop, using RAG to suggest improvements.
4. **Mock Interview:** Mistral 7B acts as the interviewer, adapting questions based on the candidate's weak points identified by the semantic engine."

## 5. Conclusion
**Speaker:** "Mintfolio represents a leap forward in recruitment tech, combining the reasoning power of Large Language Models with the precision of specialized NLP architectures like RoBERTa and custom NER. Thank you."

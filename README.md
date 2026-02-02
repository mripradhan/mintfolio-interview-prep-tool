# Mintfolio: AI-Powered Career Co-Pilot

Mintfolio is a modern, full-stack web application designed to help job seekers prepare for their careers. It leverages the power of AI to provide personalized feedback and tools, streamlining the job application process.

This project was built using Firebase Studio.

## ✨ Key Features

-   **📄 Resume Matcher**: Upload your resume and a job description to get an instant analysis of how well you match the role. The AI provides a match score and highlights key areas of alignment.
-   **🧠 Skill-Gap Analysis**: Identifies critical skills required by the job description that are missing from your resume and suggests relevant online courses and practice problems to bridge the gaps.
-   **🤖 AI Mock Interview**: Practice for interviews with an AI that generates tailored questions based on your resume and the job description. It supports voice input and provides real-time, constructive feedback on your answers.
-   **🔐 Secure & Private**: Built on Firebase, all user data is protected by strict security rules, ensuring that only you can access your personal information.

## 🚀 Tech Stack

-   **Framework**: [Next.js](https://nextjs.org/) (with App Router)
-   **Language**: [TypeScript](https://www.typescriptlang.org/)
-   **UI**: [React](https://reactjs.org/)
-   **Styling**: [Tailwind CSS](https://tailwindcss.com/)
-   **Components**: [ShadCN UI](https://ui.shadcn.com/)
-   **Authentication & Database**: [Firebase Authentication & Firestore](https://firebase.google.com/)
-   **Generative AI**: [Mistral AI](https://mistral.ai/)
-   **Deployment**: [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)

## 🛠️ Getting Started

### Prerequisites

-   Node.js (v18 or later)
-   npm, yarn, or pnpm
-   Firebase Account & Project

### Environment Variables

To run this project locally, you need to create a `.env` file in the root of the project and add your Mistral API key:

```.env
MISTRAL_API_KEY="your_mistral_api_key_here"
```

You also need to configure your Firebase project credentials in `src/firebase/config.ts`.

### Running Locally

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mintfolio-backend-fix
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Run the development server:**
    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:9002`.

## 📂 Project Structure

```
.
├── src/
│   ├── app/                # Next.js App Router pages and layouts
│   ├── components/         # Shared React components (UI, auth, dashboard)
│   ├── ai/                 # AI flows using Mistral
│   ├── context/            # React context for global state (e.g., file uploads)
│   ├── firebase/           # Firebase configuration, hooks, and providers
│   ├── hooks/              # Custom React hooks
│   ├── lib/                # Utility functions, constants, and data
│   └── ...
├── public/                 # Static assets
├── firestore.rules         # Firestore security rules
├── apphosting.yaml         # Firebase App Hosting configuration
└── ...
```

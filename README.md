# 🧠 AI-Powered Mock Test Generator CLI

A command-line utility designed to transform any subject or uploaded material into structured, high-quality Multiple Choice Questions (MCQs) for effective mock test preparation.

---

## ✨ Product Vision & Value Proposition

The goal is to move beyond simple question generation and become an **Adaptive Learning Companion**. We don't just create quizzes; we pinpoint knowledge gaps and provide a measurable path to mastery.

**Core Problem Solved:** Traditional study methods are inefficient because they lack personalized feedback and structured testing based on specific learning objectives or source material.
**Our Solution:** A CLI tool that automates the creation, validation, and interactive testing process using advanced LLM capabilities.

---

## 🗺️ Product Roadmap & Development Phases

We recommend a phased approach to minimize risk and maximize early user feedback.

### 🟢 Phase 1: Minimum Viable Product (MVP) - The Core Loop
*   **Goal:** Prove the core value: Subject $\rightarrow$ Questions $\rightarrow$ Test.
*   **Features:**
    *   CLI accepts subject/topic name (e.g., "Quantum Entanglement").
    *   Calls LM Studio to generate structured JSON output of MCQs.
    *   Basic AI self-critique validation on the generated set.
    *   Simple CLI UI for taking and scoring a quiz.
*   **Focus:** Stability, reliability, and proving the quality of the generated content.

### 🟡 Phase 2: Feature Expansion & Polish - The "Pro" Offering
*   **Goal:** Increase stickiness and justify a paid subscription.
*   **Features:**
    *   **Source Material Upload:** Allow users to upload PDFs/documents and generate questions *only* from that content (Major value-add).
    *   **Advanced Validation Engine:** Implement structured, multi-step prompting to ensure question quality (e.g., checking for plausible distractors).
    *   **Detailed Analytics:** Track performance over time: weak topics, average score per subject, and historical progress reports.
    *   **UI/UX Polish:** Enhanced CLI experience using libraries like `rich`.

### 🔴 Phase 3: Premium & Enterprise - The High-Value Services
*   **Goal:** Capture institutional revenue (B2B).
*   **Features:**
    *   **Proctoring Integration:** Real-time monitoring of the user during a mock test (e.g., detecting external materials, prolonged gaze away from screen). *Requires careful handling of privacy and permissions.*
    *   **Adaptive Learning Path:** The system analyzes performance and dynamically adjusts the next set of questions to focus exclusively on weak areas (Spaced Repetition System integration).
    *   **LMS Integration:** API endpoints for educational institutions to embed testing into their existing platforms.

---

## 💰 Monetization Strategy: The Funnel Approach

The monetization strategy is built around a **Freemium Model**, guiding users from free utility to paid subscription, and finally to enterprise licensing.

| Tier | Target User | Key Features Unlocked | Pricing Model |
| :--- | :--- | :--- | :--- |
| **FREE** (MVP) | Casual Learner / Student | Basic generation, limited daily quota (e.g., 5 quizzes/day). | $0 |
| **PRO** (Phase 2+) | Serious Student / Professional | Unlimited usage, Source Material Upload, Advanced Analytics, Priority Support. | Subscription (\$9.99 - \$29.99/month) |
| **ENTERPRISE** (Phase 3+) | Universities / Corporations | LMS Integration, Bulk Licensing, Custom Curriculum Mapping, Proctoring Suite. | Custom Quote (B2B Contract) |

### 💡 Key Monetization Principles:
1.  **The Hook:** The free tier must be *good enough* to be useful but *limited enough* to create a clear pain point that only the Pro subscription can solve (e.g., running out of daily quizzes, or needing to test on proprietary notes).
2.  **Value Ladder:** Each phase introduces exponentially higher value and complexity, justifying an increasing price point.

---

## 🛠️ Technical Considerations & Next Steps

*   **Primary Tool:** LM Studio API integration (via structured JSON output).
*   **Language Recommendation:** Python (due to excellent libraries for CLI UI (`rich`), file handling (`pypdf`, `pandas`), and AI interaction).
*   **Immediate Action Item:** Focus 100% on building the **Phase 1 MVP**. Get it working end-to-end before thinking about payments or proctoring.
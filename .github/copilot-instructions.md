# Copilot Instructions for NanoToX

## Project Overview
NanoToX is a Streamlit-based web application for AI-driven nanotoxicity prediction. The app provides user authentication (via Supabase), a modern UI, and a workflow for submitting chemical/nanomaterial data for toxicity analysis. The project is designed for academic and research use, prioritizing privacy and ethical data handling.

## Architecture & Key Files
- **Home_page.py**: Main landing page with custom UI, navigation, and informational sections. Uses Streamlit and custom HTML/CSS for layout.
- **login.py**: Handles user authentication, session state, and navigation between login, signup, prediction, and result pages. Integrates with Supabase for user management.
- **login_page.py**: Alternative login/signup UI with stricter password validation and extended user metadata (e.g., institution, country).
- **requirements.txt**: Lists Python dependencies (primarily `streamlit`).
- **.devcontainer/devcontainer.json**: Dev container setup for consistent development environments.

## Developer Workflows
- **Install dependencies:**
  ```sh
  pip install -r requirements.txt
  ```
- **Run the app locally:**
  ```sh
  streamlit run Home_page.py
  # or for login workflow:
  streamlit run login.py
  ```
- **Devcontainer:**
  The devcontainer auto-installs requirements and launches the app on port 8501.

## Project Conventions & Patterns
- **Session State:**
  - Use `st.session_state` for navigation and user state (e.g., `page`, `user`).
  - Navigation is handled by setting `st.session_state.page` and calling `st.rerun()`.
- **Authentication:**
  - Supabase credentials are loaded from `st.secrets`.
  - User objects are stored in session state after login/signup.
- **UI:**
  - Heavy use of custom HTML/CSS via `st.markdown` and `components.html` for branding and layout.
  - Images are loaded from the workspace (e.g., `nanotox1-logo.png`, `title1.png`).
- **Prediction Logic:**
  - Currently a placeholder; replace with ML model integration as needed.
- **Privacy:**
  - No user data is stored permanently; see privacy policy in the footer of `Home_page.py`.

## Integration Points
- **Supabase:** Used for authentication and user management. Requires secrets in `.streamlit/secrets.toml`.
- **Streamlit:** All UI and routing logic is built on Streamlit.

## Examples
- To add a new page, follow the session state pattern in `login.py`.
- To update the UI, use custom HTML/CSS blocks as in `Home_page.py`.

## References
- See `Home_page.py` and `login.py` for main patterns.
- For dev setup, see `.devcontainer/devcontainer.json` and `README.md`.

---
For questions, contact the project maintainer listed in the footer or open an issue.

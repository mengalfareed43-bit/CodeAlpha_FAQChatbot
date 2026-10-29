import streamlit as st

faqs = {
    "what is codealpha": "CodeAlpha is a software development company that offers IT training, internships, and real-world project experience in emerging technologies.",
    "how to submit tasks": "You need to upload your complete source code to GitHub in a repository named with your project name, record a video explanation, post it on LinkedIn, and submit via the official Google Form provided in your WhatsApp group.",
    "what are the internship perks": "Perks include an Internship Offer Letter, QR Verified Completion Certificate, Unique ID Certificate, Letter of Recommendation, Job Opportunities, and Resume Building Support.",
    "how many tasks are required": "You need to complete a minimum of 2 or 3 tasks out of the 4 given tasks to be eligible for the internship certificate.",
    "contact support": "You can contact CodeAlpha via email at services.codealpha@gmail.com or visit their website at www.codealpha.tech."
}

st.set_page_config(page_title="CodeAlpha - FAQ Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 CodeAlpha AI Internship")
st.subheader("Task 2: Chatbot for FAQs")
st.write("Select a question or ask your own!")

selected_question = st.sidebar.selectbox("Choose a question:", ["-- Select --"] + list(faqs.keys()))
user_query = st.text_input("Type your question here:", placeholder="e.g. what is codealpha")

query_to_process = ""
if selected_question != "-- Select --":
    query_to_process = selected_question
elif user_query.strip() != "":
    query_to_process = user_query.strip().lower()

if st.button("Ask Chatbot", type="primary"):
    if query_to_process:
        found = False
        for q, a in faqs.items():
            if q in query_to_process or query_to_process in q:
                st.success("Bot Response:")
                st.info(a)
                found = True
                break
        if not found:
            st.warning("No matching answer found. Please select from sidebar options.")
    else:
        st.warning("Please select or enter a question first!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Developed with ❤️ for CodeAlpha Internship</p>", unsafe_allow_html=True)
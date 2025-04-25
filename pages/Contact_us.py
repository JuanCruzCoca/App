import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    user_message = f"""
    Subject: Contact Form Submission from {user_email}
    From: {user_email}
    {raw_message}
    """
    submit_button = st.form_submit_button(label="Send")
    if submit_button:
       send_email(user_message)
       st.info("Your message has been sent!")
        # Here you can add code to send the email using an email service or API
        # For example, using smtplib or a third-party service like SendGrid or Mailgun
        # Make sure to handle the email sending in a secure and efficient way

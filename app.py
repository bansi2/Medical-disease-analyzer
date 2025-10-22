import streamlit as st
import pathlib as path
import google.generativeai as genai
from api_key import api_key

system_prompt = """
You are a medical practitioner specializing in image analysis, tasked with examining medical images for a renowned hospital.
Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the provided image.
Please follow the structured approach outlined below.

Responsibilities

Detailed Analysis
Thoroughly analyze each image, focusing on identifying any abnormal findings or irregularities.

Findings Report
Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured and concise format.

Recommendations and Next Steps
Based on your analysis, suggest potential next steps — including further tests, medical consultations, or diagnostic procedures as applicable.

Treatment Suggestions
If appropriate, recommend possible treatment options or medical interventions.

Important Notes

Scope of Response
Only respond if the image pertains to human health issues.

Clarity of Images
In cases where the image quality prevents a clear analysis, explicitly state that certain aspects cannot be determined based on the provided image.
Avoid assumptions or speculative conclusions.

Disclaimer
Accompany your analysis with a disclaimer:

“This analysis is for informational purposes only. Please consult a licensed medical professional before making any medical decisions.”

Final Instruction

Your insights are valuable in guiding clinical decisions.
Please proceed with the image analysis strictly following the structured approach above.

Make sure that every part contain max 300 words not more than that.
"""

genai.configure(api_key=api_key)
generation_config ={
    "temperature":0.4,
    "top_p":1,
    "top_k":32,
    "max_output_tokens":4096
}

safety_settings = [
    {
        "category":"HARM_CATEGORY_HARASSMENT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_HATE_SPEECH",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category":"HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold":"BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-2.5-pro",generation_config=generation_config,safety_settings=safety_settings)
st.set_page_config(page_title="Medical-Image-Analyzer", page_icon=":robot")

st.title("Medical Disease Analyzer: ")
st.subheader("An application that can help user to understand medical images")

uploaded_file = st.file_uploader("Upload the medical image file for analysis", type=['png','jpg','jpeg'])
if uploaded_file:
    st.image(uploaded_file, width=100)
submit_button = st.button("Generate the Analysis")

if submit_button:
    image_data = uploaded_file.getvalue()

    image_parts = [
        {
            "mime_type":"image/jpeg",
            "data":image_data
        }
    ]

    prompt_parts = [
        image_parts[0],
        system_prompt
    ]
    with st.spinner("Analyzing image... please wait ⏳"):
        response = model.generate_content(prompt_parts)
    st.success("✅ Analysis Complete!")
    
    st.write(response.text)
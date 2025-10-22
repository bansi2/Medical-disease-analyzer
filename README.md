🩺 Medical Image Analyzer

An AI-powered Streamlit application that analyzes medical images (like X-rays, MRIs, CT scans, etc.) to help identify potential anomalies, diseases, or health issues.
The app uses Google Gemini 2.5 Pro to generate structured medical analysis reports, including findings, recommendations, and treatment suggestions.

🚀 Features

🧠 AI-Powered Medical Image Analysis using Google’s Gemini model

📋 Structured Output including:

  1)Detailed analysis of findings

  2)Clear anomaly/disease documentation

Recommended next steps and treatments

  ⚙️ Dynamic Image Uploads (supports .png, .jpg, .jpeg)

  🌀 Loading Spinner while model processes the image

  ✅ Safety & Compliance — includes disclaimers and avoids speculative responses

  💬 Streamlit UI for easy interaction

🧩 Tech Stack
Component	Description
Python 3.10+	Programming language
Streamlit	For building interactive web UI
Google Generative AI SDK	For integrating Gemini 2.5 Pro model
Pathlib	For file handling
Gemini 2.5 Pro	Core AI model used for medical analysis

▶️ Usage

Run the Streamlit app
streamlit run app.py
Upload a medical image
Accepted formats: .png, .jpg, .jpeg
Click on “Generate Analysis”

A detailed, structured medical report will be displayed


🧠 System Prompt Used

The AI model is guided by a structured system prompt that ensures consistent and medically responsible output.
It includes:

1)Detailed analysis

2)Findings report

3)Recommendations & next steps

4)Treatment suggestions

5)Image clarity and response scope checks

Disclaimer: “This analysis is for informational purposes only. Please consult a licensed medical professional before making any medical decisions.”

⚠️ Disclaimer

This tool is for educational and informational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult a qualified healthcare provider for any medical concerns.

🤝 Contributing

Contributions are welcome!
If you'd like to improve the app or add new features, feel free to fork the repo and submit a pull request.

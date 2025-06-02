const API_URL = "https://farmsight-api.onrender.com/"; // Replace this with your actual backend URL

async function analyzeImage() {
  const fileInput = document.getElementById("imageInput");
  const resultText = document.getElementById("imageResult");

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  const response = await fetch(`${API_URL}/api/analyze-image`, {
    method: "POST",
    body: formData
  });

  const result = await response.json();
  resultText.innerText = JSON.stringify(result);
}

async function askQuestion() {
  const input = document.getElementById("questionInput").value;
  const resultText = document.getElementById("qaResult");

  const response = await fetch(`${API_URL}/api/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: input })
  });

  const result = await response.json();
  resultText.innerText = result.answer;
}

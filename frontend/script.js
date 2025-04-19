async function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    const resultDiv = document.getElementById("result");

    if (!fileInput.files.length) {
        resultDiv.innerHTML = "Please select a file.";
        return;
    }

    const formData = new FormData();
    formData.append("resume", fileInput.files[0]);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();
        if (data.success) {
            resultDiv.innerHTML = `Resume is classified as: ${data.classification}`;
        } else {
            resultDiv.innerHTML = "Error classifying resume.";
        }
    } catch (error) {
        resultDiv.innerHTML = "Failed to upload resume.";
    }
}

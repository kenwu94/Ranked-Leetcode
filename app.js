const editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    lineNumbers: true,
    mode: 'python',
    theme: 'default'
});

async function executeCode() {
    const code = editor.getValue();
    const response = await fetch("http://localhost:8000/execute", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ language: "python", code: code })
    });
    const result = await response.json();
    document.getElementById("output").textContent = result.output || result.error;
}

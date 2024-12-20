const editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    lineNumbers: true,
    mode: 'python',
    theme: 'default'
});

async function executeCode() {
    const code = editor.getValue();
    console.log("Code to execute:", code);  // Debugging line
    const response = await fetch("http://localhost:8000/execute", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ language: "python", code: code })
    });
    const result = await response.json();
    console.log("Execution result:", result);  // Debugging line
    document.getElementById("output").textContent = result.output || result.error;
    document.getElementById("output").textContent += `\nExecution Time: ${result.execution_time} seconds`;
}



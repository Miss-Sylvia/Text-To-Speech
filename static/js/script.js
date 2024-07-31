document.getElementById('speak-button').addEventListener('click', function(){
    var text = document.getElementById('text-input').value;
    var language = document.getElementById('language-select').value;


    if ('speechSynthesis' in window) {
        var utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = language;
        window.speechSynthesis.speak(utterance);
    } else {
        console.log('Speech synthesis not supported');
        
        serverSideSpeech(text, language);
    }
});

function serverSideSpeech(text, language) {
    fetch('/speak', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'text=' + encodeURIComponent(text) + '&language=' + encodeURIComponent(language)
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log('Speech completed');
        } else {
            console.log('Speech failed:', data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
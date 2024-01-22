
console.log("works")


document.addEventListener('addInput', function() {

    document.getElementById('SubmitBtn').addEventListener('click', function() {
        
        console.log('hello my friend')
        
        var inputArea = document.getElementById('inputArea');
        var newInput = document.createElement('input');
        newInput.type = 'text';
        newInput.name = 'inputs[]';
        inputArea.appendChild(newInput);
    });

});

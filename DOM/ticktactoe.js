var restart = document.querySelector('#restart');
var squares = document.querySelectorAll('td');

function clearsquares(){
    for(var i = 0; i < squares.length; i++){
        squares[i].textContent = '';
    }
}

function checkSquares(){
    if(this.textContent === ''){
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent = 'O';
    }else{
        this.textContent = ''
    }
}

restart.addEventListener('click', clearsquares);
for(var i = 0; i < squares.length; i++){
    squares[i].addEventListener('click', checkSquares);
}
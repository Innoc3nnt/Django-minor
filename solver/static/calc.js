radio = document.getElementsByName('palette');
size = document.getElementById('size').value;
palette = 1;
for (var i=0; i<radio.length; i++)
{
    radio[i].onchange = calc;
}

function sizechange()
{
    size = document.getElementById('size').value;
    document.getElementById('price').innerText = size * palette + ' руб.';
}

function calc()
{
    console.log(this.value);
    palette = this.value;
    document.getElementById('price').innerText = size * palette + ' руб.';
    console.log(price);
}
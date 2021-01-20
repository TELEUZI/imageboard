for (let i = 0; i < document.querySelectorAll('.zz').length; i++) {
    let g = document.querySelectorAll('.zz')[i];
    g.onclick = function() {
        let zzz = document.querySelectorAll('.post')[i];
        zzz.classList.toggle('close');
    }
}
let texts = document.querySelectorAll('.thread-text');

for (let text of texts) {
    let z = text.textContent;
    let re = />>\d+(?!\d)(?!\<)/;
    let i = 0;
    while (z.match(re) !== null) {
        let torepl = re.exec(z)
        z = z.replace(re, `<a href ='#${torepl[0].slice(2)}'> >>${torepl[0].slice(2)}</a>`);
    }
    text.innerHTML = z;
}
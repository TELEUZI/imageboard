var app = new Vue({
    el: '#app',
    delimiters: ['${', '}'],
    data: {
        thread_name: "",
        username: "",
        thread_text: "",
        isClose: false,
        message: 'Привет, Vue!',
        mes: 'hi',
        threads: [{
            theme: "new_thread_1",
            text: "HI EVERYONE!",
            close: false
        }, {
            theme: "new_thread_2",
            text: "HI EVERYONE!",
            close: false
        }, {
            theme: "new_thread_3",
            text: "HI EVERYONE!",
            close: false
        }, {
            theme: "new_thread_4",
            text: "HI EVERYONE!",
            close: false
        }],


    },
    methods: {
        getsucked: function(params) {
            alert("1111")
        },
        func: function(par) {
            par.close = !par.close
        },
        f: function(par) {
            fetch('http://127.0.0.1:5000/board')
                .then((response) => {
                    console.log(response)
                    if (response.ok) {
                        return response.json();
                    }
                    throw new Error('Network response was not ok');
                })
                .then((json) => {
                    this.threads.push({
                        theme: json[0],
                        text: json[2],
                        close: false
                    });
                    console.log(json)
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }
});
for (let i = 0; i < document.querySelectorAll('.zz').length; i++) {
    console.log(i)
    let g = document.querySelectorAll('.zz')[i]
    g.onclick = function() {
        let zzz = document.querySelectorAll('.main')[i]
        zzz.classList.toggle('close')
    }
}
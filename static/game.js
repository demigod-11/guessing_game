document.addEventListener("DOMContentLoaded", function(){
    var items = document.getElementsByClassName('game');
    let high = 100
    let low = 0
    tries = 6

    while(tries){
        let less = document.getElementById("#less");
        let large = document.getElementById("#large");
        let mid = Math.floor((high + low) / 2)
        document.querySelector("#guess").innerText = mid;
        document.querySelector("#tries").innerText = tries;
        less.addEventListener('click', function(){
            low = mid;
            tries--
            document.querySelector("#guess").innerText = mid;
        })
        large.addEventListener('click', function(){
            high = mid;
            tries--
            document.querySelector("#guess").innerText = mid;
        })

    }
})
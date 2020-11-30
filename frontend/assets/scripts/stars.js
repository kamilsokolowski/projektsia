//initial setup
        document.addEventListener('DOMContentLoaded', function(){
            let stars = document.querySelectorAll('.star');
            stars.forEach(function(star){
                star.addEventListener('click', setRating);
            });

            let rating = parseInt(document.querySelector('.stars').getAttribute('data-rating'));
            let target = stars[rating - 1];
            target.dispatchEvent(new MouseEvent('click'));
        
        });

        function setRating(ev){
            let span = ev.currentTarget;
            let stars = document.querySelectorAll('.star');
            let match = false;
            let grade = 0;
            stars.forEach(function(star, index){
                if(match){
                    star.classList.remove('rated');
                }else{
                    star.classList.add('rated');
                }
                //are we currently looking at the span that was clicked
                if(star === span){
                    match = true;
                    grade = index + 1;
                }
            });
            document.querySelector('.stars').setAttribute('data-rating', grade);
            document.getElementById("mark").value = grade;
            if (grade == 1)
                document.getElementById("id1").innerHTML = grade;
            if (grade == 2)
                document.getElementById("id1").innerHTML = "Oceniłeś zdarzenie na 2";
            if (grade == 3)
                document.getElementById("id1").innerHTML = "Oceniłeś zdarzenie na 3";
            if (grade == 4)
                document.getElementById("id1").innerHTML = "Oceniłeś zdarzenie na 4";
            if (grade == 5)
                document.getElementById("id1").innerHTML = "Oceniłeś zdarzenie na 5";
            document.getElementById("send").click()
                
        }
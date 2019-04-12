$(document).ready(()=>{
    main.init();
    main.onCreate();
});

var main = main || {}
main = (()=>{
    let avg_temp,min_temp,max_temp,rain_fall;

    let init = () =>{
        avg_temp = $('#avg_temp');
        min_temp = $('#min_temp');
        max_temp = $('#max_temp');
        rain_fall = $('#rain_fall');
    };
    let onCreate =()=>{
        setContentView();
    };
    let setContentView =()=>{
        login();
        predict_price()

        $('#login_btn').click(e=>{
            alert('로그인 로그인 눌렀다');

        })




    };
    let cleardata= ()=>{
        avg_temp.val('');
        min_temp.val('');
        max_temp.val('');
        rain_fall.val('');
    };

    let predict_price =()=>{
           $('#result_btn').click(e=>{
            e.preventDefault();
        alert('평균은 ' + avg_temp.val() +
            min_temp.val() + max_temp.val() + rain_fall.val())
           /* $.getJSON($SCRIPT_ROOT+'/calc',x,d=>{
                    if (d.result.toString().length>13){
                        digitError();
                    } else{
                        alert(d.result)
                    }
                });*/
            })
    }
    let login=()=>{


    }

    return {init : init,onCreate : onCreate}
})();
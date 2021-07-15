
const url=window.location.href
const searchForm=document.getElementById('search-form')
const searchInput=document.getElementById('search')
const resultsBox=document.getElementById('results-box')

const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value


const sendSearchData=(pro)=>{
    $.ajax({
        type:'POST',
        url: '/search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'pro':pro,
        },
        success: (res)=> {
            console.log(res.data)
            const data=res.data
            if(Array.isArray(data)){
                resultsBox.innerHTML =""
                data.forEach(pro=> {
                    resultsBox.innerHTML += `
                    <a href="" class="item">
                        <div class="row mt-2 mb-2">
                            
                            <div class="col-12">
                            <h5>${pro.name}</h5>

                            </div>
                        </div>
                    </a><br>
                    `
                })
            }
            else{
                if(searchInput.value.length>0)
                {
                    resultsBox.innerHTML=res.data
                }
                else{
                    resultsBox.classList.add('notvisible')
                }
            }
        },
        error: (err)=> {
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup',e=>{
    console.log(e.target.value)
    if(resultsBox.classList.contains('notvisible')){
        resultsBox.classList.remove('notvisible')
    }
    sendSearchData(e.target.value)
})

console.log(searchInput)
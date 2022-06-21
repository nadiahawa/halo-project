const getAuth = async () => {
    const clientId = '29ec436ab3904eb2ac62058b4e5cbdcd';
    const clientSecret = '2eee41ba144a460089135fc78510bf3c';
    const encodedString = btoa(clientId + ':' + clientSecret)
    const response = await fetch('https://accounts.spotify.com/api/token',
    {
        method: 'POST',
        headers: {
            'Authorization' : `Basic ${encodedString}`,
            'Content-Type' : 'application/x-www-form-urlencoded'
        },
        body: 'grant_type=client_credentials'
    }
    
    );

    let token = await response.json();
    console.log(token);
    return token.access_token
}

const loadToken = async () => {
    const token = await getAuth();
    console.log(token);
    return token

}

const getSong = async () => {
    const token = await loadToken();
    let data = await fetch(`https://api.spotify.com/v1/search?type=track&q=track:bluff+artist:kelela&limit=1`,
    {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${token}`
        }
    });
    data = await data.json();
    console.log(data);
    console.log(data.tracks.items[0].preview_url);
    let audioobj = new Audio(data.tracks.items[0].preview_url);
    audioobj.play();
}

let playbuttony = document.querySelector('#playbutton1')
playbuttony.addEventListener('click', ()=> {getSong();});


const getSong2 = async () => {
    const token = await loadToken();
    let data = await fetch(`https://api.spotify.com/v1/search?type=track&q=track:out%20getting%20ribs+artist:king%20krule&limit=1`,
    {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${token}`
        }
    });
    data = await data.json();
    console.log(data);
    console.log(data.tracks.items[0].preview_url);
    let audioobj = new Audio(data.tracks.items[0].preview_url);
    audioobj.play();
}

let playbuttony2 = document.querySelector('#playbutton2')
playbuttony2.addEventListener('click', ()=> {getSong2();});


const getSong3 = async () => {
    const token = await loadToken();
    let data = await fetch(`https://api.spotify.com/v1/search?type=track&q=track:submission+artist:gorillaz&limit=1`,
    {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${token}`
        }
    });
    data = await data.json();
    console.log(data);
    console.log(data.tracks.items[0].preview_url);
    let audioobj = new Audio(data.tracks.items[0].preview_url);
    audioobj.play();
}

let playbuttony3 = document.querySelector('#playbutton3')
playbuttony3.addEventListener('click', ()=> {getSong3();});




const getSong4 = async () => {
    const token = await loadToken();
    let data = await fetch(`https://api.spotify.com/v1/search?type=track&q=track:voices+artist:flume&limit=1`,
    {
        method: 'GET',
        headers: {
            'Content-Type' : 'application/json',
            'Authorization' : `Bearer ${token}`
        }
    });
    data = await data.json();
    console.log(data);
    console.log(data.tracks.items[0].preview_url);
    let audioobj = new Audio(data.tracks.items[0].preview_url);
    audioobj.play();
}

let playbuttony4 = document.querySelector('#playbutton4')
playbuttony4.addEventListener('click', ()=> {getSong4();});



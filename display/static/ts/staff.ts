async function setSidePage(hide) {
    let sidepage = document.getElementById("sidepage");
    if (hide)
        sidepage.className = "absolute top-0 right-0 w-0 h-[100%] overflow-hidden pt-[50px] transition-all duration-300"
    else
        sidepage.className = "absolute top-0 right-0 w-[50%] h-[100%] overflow-hidden pt-[50px] transition-all duration-300"
}

async function magic(volname) {
    let voldata = await JSON.parse(await (await fetch("/staff?" + new URLSearchParams({
        volname: volname
    }).toString())).text());
    let userinfo = document.getElementById("userinfo");
    userinfo.innerHTML = '';

    let pageHTML = `
        <div>
            <div class="w-full flex flex-col items-center text-white">
                <div class="flex flex-col items-center mb-12">
                    <p class="text-3xl">${voldata.vol.name}</p>
                    <p class="text-xl text-neutral-300">${voldata.vol.email}</p>
                </div>
                <div class="flex gap-7">
                    <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px]">
                        <p>Total Hours</p>
                        <p class="text-3xl w-[300px]"><b>${voldata.total_hr}</b></p>
                    </div>
                    <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px]">
                        <p>Number of Sessions</p>
                        <p class="text-3xl w-[300px]"><b>${voldata.num_seshs}</b></p>
                    </div>
                </div>
                <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px] mt-5">
                    <p>Average Hours per Session</p>
                    <p class="text-3xl w-[300px]"><b>${Math.round(voldata.avg_hr * 10) / 10}</b></p>
                </div>
            </div>
            <div class="flex flex-col items-center">
                <p class="text-3xl mb-5 mt-12">Sessions</p>
                <div class="border p-5 flex flex-col gap-5 w-[30vw] h-[300px] overflow-y-scroll rounded-xl" id="seshsDiv">
                </div>
            </div>
        </div>
    `;

    let parser = new DOMParser();
    const doc = parser.parseFromString(pageHTML, 'text/html');
    const element = doc.body.firstChild;
    userinfo?.appendChild(element);

    let seshsDiv = document.getElementById("seshsDiv");

    for (let i = 0; i < voldata.num_seshs; ++i) {
        let seshHTML = `
            <div class="p-3 bg-neutral-800 rounded-lg">
                <p class="text-neutral-300">${voldata.seshs[i].beganAt}</p>
                <p class="text-3xl"><b>${voldata.seshs[i].length}h</b></p>
            </div>
        `
        const doc = parser.parseFromString(seshHTML, 'text/html');
        const element = doc.body.firstChild;
        seshsDiv?.appendChild(element);
    }

}

/*
    <div class="w-full flex flex-col items-center mt-[50px] text-white">
        <div class="flex flex-col items-center my-12">
            <p class="text-3xl">{{ vol.name }}</p>
            <p class="text-xl text-neutral-300">{{ vol.email }}</p>
        </div>
        <div class="flex gap-7">
            <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px]">
                <p>Total Hours</p>
                <p class="text-3xl"><b>{{ total_hr }}</b></p>
            </div>
            <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px]">
                <p>Number of Sessions</p>
                <p class="text-3xl"><b>{{ num_seshs }}</b></p>
            </div>
            <div class="text-xl bg-neutral-800 p-3 rounded-lg w-[300px]">
                <p>Average Hours per Session</p>
                <p class="text-3xl"><b>{{ avg_hr|floatformat:1 }}</b></p>
            </div>
        </div>
        <div>
            <p class="text-3xl mb-5 mt-12">Sessions</p>
            <div class="border p-5 flex flex-col gap-5 w-[30vw] h-[400px] overflow-y-scroll rounded-xl">
                {% for sesh in seshs %}
                    <div class="p-3 bg-neutral-800 rounded-lg">
                        <p class="text-neutral-300">{{ sesh.beganAt }}</p>
                        <p class="text-3xl"><b>{{ sesh.length }}h</b></p>
                    </div>
                {% endfor %}
            </div>
        </div>
    </div>
*/
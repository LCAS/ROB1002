const socket = new WebSocket('ws://' + location.host + '/command');

socket.addEventListener('message', ev => {
    console.log("(app.js) 📣 " + ev.data)
});

function sendCmd(cmd) {
    console.log("Going " + cmd)
    socket.send(cmd);
}

// Menu Toggle
let isMenuOpen = false;
const robot = document.getElementById('robot')
const options = document.getElementById('options')

document.getElementById('menu').onclick = ev => {
    ev.preventDefault();
    
    if (isMenuOpen) {
        // close menu, open robot
        robot.style.display = "flex";
        options.style.display = "none";
        isMenuOpen = false;
    } else {
        // open menu, close robot
        robot.style.display = "none";
        options.style.display = "flex";
        isMenuOpen = true;
    }
};

// On Screen Controls
document.getElementById('left').onclick = ev => {
    ev.preventDefault();
    sendCmd("left")
};

document.getElementById('right').onclick = ev => {
    ev.preventDefault();
    sendCmd("right");
};

document.getElementById('up').onclick = ev => {
    ev.preventDefault();
    sendCmd("up");
};

document.getElementById('down').onclick = ev => {
    ev.preventDefault();
    sendCmd("down");
};

document.getElementById('stop').onclick = ev => {
    ev.preventDefault();
    sendCmd("stop");
};


// WASD
document.addEventListener('keydown', function (event) {
    if (event.code === 'KeyW') {
        sendCmd('up');
    } else if (event.code === 'KeyA') {
        sendCmd('left');
    } else if (event.code === 'KeyS') {
        sendCmd('down');
    } else if (event.code === 'KeyD') {
        sendCmd('right');
    } else if (event.code === 'KeyX') {
            sendCmd('stop');
    } else if (event.code === 'Enter') {
        return;
    }
});
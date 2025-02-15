const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const resultDiv = document.getElementById('result');

// カメラの設定
navigator.mediaDevices.getUserMedia({ 
    video: { 
        facingMode: "environment",
        width: { ideal: 1280 },
        height: { ideal: 720 }
    } 
})
.then(function(stream) {
    video.srcObject = stream;
    video.setAttribute('playsinline', true);
    video.play();
    requestAnimationFrame(tick);
})
.catch(function(err) {
    console.error("カメラの起動に失敗しました:", err);
    resultDiv.textContent = "カメラの起動に失敗しました。カメラへのアクセスを許可してください。";
});

function tick() {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height, {
            inversionAttempts: "dontInvert",
        });

        if (code) {
            console.log("QRコードを検出:", code.data);
            
            // QRコードの内容が有効なURLかチェック
            try {
                const url = new URL(code.data);
                resultDiv.innerHTML = `
                    <p>QRコードを検出しました！</p>
                    <p>URL: ${code.data}</p>
                    <button onclick="window.location.href='${code.data}'">商品ページへ移動</button>
                `;
                // QRコードを検出したら一時停止
                video.pause();
                return;
            } catch (e) {
                resultDiv.textContent = "無効なURLが含まれているQRコードです。";
            }
        }
    }
    requestAnimationFrame(tick);
}

// 結果をリセットしてスキャンを再開
resultDiv.addEventListener('click', function() {
    if (video.paused) {
        resultDiv.textContent = "";
        video.play();
        requestAnimationFrame(tick);
    }
});

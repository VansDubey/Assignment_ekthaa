document.addEventListener("DOMContentLoaded", () => {
    loadCatalogue();
});

function loadCatalogue() {
    fetch("/catalogue")
        .then(res => res.json())
        .then(data => {
            const products = data.products;
            const container = document.getElementById("catalogue_container");

            container.innerHTML = "";  // clear old data

            products.forEach(p => {
                container.innerHTML += `
                    <div class="product-card">
                        <img src="${p.image_url}" class="product-img" />
                        <h3>${p.name}</h3>
                        <p>₹${p.selling_price}</p>
                    </div>
                `;
            });
        })
        .catch(err => console.error("Error loading catalogue:", err));
}






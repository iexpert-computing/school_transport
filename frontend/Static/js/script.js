<script>
    let map = L.map('map').setView([-23.55052, -46.633308], 13); // Inicializa o mapa

    // Adiciona um mapa base do OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    async function fetchRoute() {
        try {
                let response = await fetch("http://127.0.0.1:8000/rota", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    origin: [-23.55052, -46.633308],
                    destinations: [
                        [-23.56168, -46.62529],
                        [-23.54747, -46.63611],
                        [-23.56272, -46.65095]
                    ]
                })
            });

            let data = await response.json();
            console.log("Rota recebida:", data);

            if (data.geometry) {
                let coordinates = data.geometry.coordinates.map(coord => [coord[1], coord[0]]); // Inverter [lng, lat] para [lat, lng]

                // Remove camadas anteriores do mapa (se existirem)
                if (window.routeLayer) {
                    map.removeLayer(window.routeLayer);
                }

                // Adiciona a linha da rota ao mapa
                window.routeLayer = L.polyline(coordinates, { color: 'blue', weight: 4 }).addTo(map);

                // Ajusta a visualização do mapa para a rota
                map.fitBounds(window.routeLayer.getBounds());
            } else {
                console.error("Nenhuma geometria encontrada na resposta da API.");
            }
        } catch (error) {
            console.error("Erro ao buscar a rota:", error);
        }
    }

    window.fetchRoute = fetchRoute; // Disponibiliza a função no escopo global
</script>

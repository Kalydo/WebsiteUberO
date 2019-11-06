
        var map;
        // Initialize and add the map
        function createMap(listener) {
            var options = {
                center: { lat: 47.5592525, lng: 7.5783315},
                zoom: 9
            };
            map = new google.maps.Map(document.getElementById('map'), options);

            var input = document.getElementById('search');
            var input1 = document.getElementById('search1');
            var searchBox = new google.maps.places.Searchbox(input);
            var searchBox1 = new google.maps.places.Searchbox(input1);

            // noinspection JSDeprecatedSymbols
            map.addListener('bound_changed', function () {
                searchBox.setBounds(map.getBounds());
                searchBox1.setBounds(map.getBounds());
            });

            var markers = [];
            // noinspection JSDeprecatedSymbols
            map.addListener('place_changed', function() {
                var places = getPlaces();

                if(places.length === 0)
                    return;
                markers.foreach(function (m) { m.setMap(null)});
                markers = [];

                var bounds = new google.maps.LatLngBounds();

                places.forEach(function (p) {
                    if(!p.geometry)
                        return;

                    markers.push(new google.maps.Marker({
                        map: map,
                        title: p.name,
                        position: p.geometry.location
                    }));

                    if(p.geometry.viewport)
                        bounds.union(p.geometry.viewport);
                    else
                        bounds.extend(p.geometry.location);
                });
                map.fitBounds(bounds);
            });
        }
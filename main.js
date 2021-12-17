function getFrontpageGamesData() {
    let data = [];
    containers = document.getElementsByClassName('games-list-container')
    for (c of containers) {
        header = c.getElementsByClassName('container-header')[0]
            .getElementsByTagName('h3')[0].innerText;
        game_card_links = c.getElementsByClassName('game-card-link');
        place_ids = [];
        for (game_card_link of game_card_links) {
            link = game_card_link.href;
            start = link.indexOf('PlaceId=');
            end = link.indexOf('&', start);
            place_ids.push(link.substring(start + 8, end));
        }
        data.push({
            'header': header,
            'places': place_ids
        });
    }
    console.log(JSON.stringify(data))
}
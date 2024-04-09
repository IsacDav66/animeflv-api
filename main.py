from flask import Flask, jsonify, request
from animeflv import AnimeFLV, EpisodeFormat

app = Flask(__name__)
animeflv = AnimeFLV()

@app.route('/')
def index():
    return 'Welcome to the animeflv-api!!'

@app.route('/search')
def search_anime():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    try:
        results = animeflv.search(query=query)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/anime/<anime_id>')
def get_anime_info(anime_id):
    try:
        anime_info = animeflv.get_anime_info(anime_id)
        return jsonify(anime_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/anime/<anime_id>/episodes/<int:episode>')
def get_episode_links(anime_id, episode):
    try:
        links = animeflv.get_links(id=anime_id, episode=episode, format=EpisodeFormat.Subtitled)
        return jsonify(links)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/anime/latest')
def get_latest_animes():
    try:
        latest_animes = animeflv.get_latest_animes()
        return jsonify(latest_animes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/episodes/latest')
def get_latest_episodes():
    try:
        latest_episodes = animeflv.get_latest_episodes()
        return jsonify(latest_episodes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

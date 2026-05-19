from flask import Flask, render_template, request, jsonify
from hotel_logic import HotelSystem, Room, Guest

app = Flask(__name__)
system = HotelSystem()


@app.route('/')
def home():
    return render_template('index.html')


# --- API РУЧКИ ---

@app.route('/api/rooms', methods=['GET', 'POST'])
def handle_rooms():
    if request.method == 'POST':
        num = int(request.args.get('number', 0))
        r_type = request.args.get('type', 'Unknown')
        price = float(request.args.get('price', 0.0))
        system.add_room(Room(num, r_type, price))
        return "✅ Room added!"
    return jsonify(system.get_all_rooms())


@app.route('/api/guests', methods=['GET', 'POST'])
def handle_guests():
    if request.method == 'POST':
        g_id = int(request.args.get('id', 0))
        name = request.args.get('name', 'Unknown')
        phone = request.args.get('phone', '')
        city = request.args.get('city', '')
        system.add_guest(Guest(g_id, name, phone, city))
        return "✅ Guest added!"
    return jsonify(system.get_all_guests())


@app.route('/api/bookings', methods=['GET', 'POST'])
def handle_bookings():
    if request.method == 'POST':
        b_id = int(request.args.get('bId', 0))
        room_num = int(request.args.get('roomNum', 0))
        guest_id = int(request.args.get('guestId', 0))
        nights = int(request.args.get('nights', 1))

        # Вызываем логику бронирования
        total_price = system.create_booking(b_id, room_num, guest_id, nights)

        if total_price:
            return f"✅ Booking created! Total cost: {total_price} KZT."
        return "❌ Booking failed (Room unavailable or not found)."

    return jsonify(system.get_all_bookings())


@app.route('/api/rooms/sorted')
def get_sorted():
    return jsonify(system.sort_rooms())


@app.route('/api/rooms/filter')
def filter_rooms():
    return jsonify(system.filter_rooms(request.args.get('type', '')))


@app.route('/api/rooms/<int:number>', methods=['GET', 'DELETE'])
def manage_room(number):
    if request.method == 'DELETE':
        system.delete_room(number)
        return "✅ Room deleted."
    room = system.find_room(number)
    return jsonify(room) if room else jsonify({"error": "Not found"}), 404


@app.route('/api/rooms/<int:number>/price', methods=['PUT'])
def update_price(number):
    new_price = float(request.args.get('price', 0))
    if system.update_price(number, new_price):
        return "✅ Price updated."
    return "❌ Error: Room not found."


@app.route('/api/rooms/<int:number>/status', methods=['PUT'])
def update_status(number):
    if system.update_status(number, True):
        return "✅ Status updated."
    return "❌ Error: Room not found."


if __name__ == '__main__':
    app.run(debug=True, port=8888)
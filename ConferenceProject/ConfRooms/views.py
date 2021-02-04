from django.shortcuts import render, redirect, get_object_or_404

from django.views import View
from .models import Room, Booking
from datetime import date, datetime


class HomeView(View):
    def get(self, request):
        return render(request, 'ConfRooms/base.html')


class AddRoom(View):
    def get(self, request):
        return render(request, 'ConfRooms/add_edit_room.html')

    def post(self, request):
        new_room = Room()
        registered_rooms = Room.objects.all()
        room_names = [room.name for room in registered_rooms]

        if request.POST.get('room_name') in room_names:
            return render(request, 'ConfRooms/add_edit_room.html', {'error': 'Name already exists'})

        new_room.name = request.POST.get('room_name')
        new_room.capacity = request.POST.get('capacity')
        new_room.projector = True if request.POST.get('projector') else False

        new_room.save()
        return render(request, 'ConfRooms/add_edit_room.html', {'room_names': room_names,})


class ShowRooms(View):
    def get(self, request):
        registered_rooms = Room.objects.all()
        return render(request, 'ConfRooms/show_rooms.html', {'rooms': registered_rooms,})


class DeleteRoom(View):
    def get(self, request, room_pk):
        room_to_delete = get_object_or_404(Room, pk=room_pk)
        return render(request, 'ConfRooms/delete_room.html', {'room_to_delete': room_to_delete})

    def post(self, request, room_pk):
        room_to_delete = get_object_or_404(Room, pk=room_pk)
        if request.POST.get('delete'):
            room_to_delete.delete()
        return redirect('/room/list/')


class EditRoom(View):
    def get(self, request, room_pk):
        room_to_edit = get_object_or_404(Room, pk=room_pk)
        return render(request, 'ConfRooms/add_edit_room.html', {'room_to_edit': room_to_edit})

    def post(self, request, room_pk):
        registered_rooms = Room.objects.all()
        room_names = [room.name for room in registered_rooms]
        room_to_edit = get_object_or_404(Room, pk=room_pk)
        room_to_edit.name = request.POST.get('room_name')

        if request.POST.get('room_name') in room_names:
            return render(request, 'ConfRooms/add_edit_room.html', {'error': 'Name already exists'})

        room_to_edit.capacity = request.POST.get('capacity')
        room_to_edit.projector = True if request.POST.get('projector') else False
        room_to_edit.save()
        return redirect('/room/list/')


class ReserveRoom(View):
    def get(self, request, room_pk):
        room_to_reserve = get_object_or_404(Room, pk=room_pk)
        return render(request, 'ConfRooms/reserve_room.html', {'room': room_to_reserve.name})

    def post(self, request, room_pk):
        date_now = date.today()
        booking_date = datetime.strptime(request.POST.get('reservation_date'), '%Y-%m-%d').date()

        if booking_date >= date_now:
            if not Booking.objects.filter(date=booking_date, room=room_pk):
                new_booking = Booking()
                new_booking.date = booking_date
                new_booking.comment = request.POST.get('comment')
                new_booking.room = get_object_or_404(Room, pk=room_pk)
                new_booking.save()
                return render(request, 'ConfRooms/reserve_room.html', {'room': f"Room {new_booking.room.name} succesfully reserved", })
            else:
                return render(request, 'ConfRooms/reserve_room.html', {'room': f"Selected date is not available for this room", })

        return render(request, 'ConfRooms/reserve_room.html', {'room': f"Date is invalid",})









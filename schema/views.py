from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

def index(request):
    return render(request, 'schema/index.html')

from .models import Accessory, Archive, Battery, BulkFilm, Camera, CameraModel, Developer, Enlarger, FilmStock, Filter
from .models import Flash, FlashProtocol, Format, Lens, LensModel, Manufacturer
from .models import MeteringType, Mount, MountAdapter, NegativeSize, Order, PaperStock, Person, Print, Toning
from .models import Process, Repair, Scan, Negative, Film, Series, ShutterSpeed, Teleconverter, Toner

class AccessoryList(generic.ListView):
  model = Accessory
  template_name = 'schema/list.html'

class ArchiveList(generic.ListView):
  model = Archive
  template_name = 'schema/list.html'

class BatteryList(generic.ListView):
  model = Battery
  template_name = 'schema/list.html'

class BulkFilmList(generic.ListView):
  model = BulkFilm
  template_name = 'schema/list.html'

class CameraList(generic.ListView):
  model = Camera
  template_name = 'schema/list.html'

class CameraDetail(generic.DetailView):
  model = Camera
  #template_name = 'schema/detail.html'

class CameraCreate(CreateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/create.html'

class CameraUpdate(UpdateView):
  model = Camera
  fields = '__all__'
  template_name = 'schema/update.html'

class CameraModelList(generic.ListView):
  model = CameraModel
  template_name = 'schema/list.html'

class DeveloperList(generic.ListView):
  model = Developer
  template_name = 'schema/list.html'

class EnlargerList(generic.ListView):
  model = Enlarger
  template_name = 'schema/list.html'

class FilmStockList(generic.ListView):
  model = FilmStock
  template_name = 'schema/list.html'

class FilterList(generic.ListView):
  model = Filter
  template_name = 'schema/list.html'

class FlashList(generic.ListView):
  model = Flash
  template_name = 'schema/list.html'

class FlashProtocolList(generic.ListView):
  model = FlashProtocol
  template_name = 'schema/list.html'

class FormatList(generic.ListView):
  model = Format
  template_name = 'schema/list.html'

class LensList(generic.ListView):
  model = Lens
  template_name = 'schema/list.html'

class LensModelList(generic.ListView):
  model = LensModel
  template_name = 'schema/list.html'

class ManufacturerList(generic.ListView):
  model = Manufacturer
  template_name = 'schema/list.html'

class MeteringTypeList(generic.ListView):
  model = MeteringType
  template_name = 'schema/list.html'

class MountList(generic.ListView):
  model = Mount
  template_name = 'schema/list.html'

class MountAdapterList(generic.ListView):
  model = MountAdapter
  template_name = 'schema/list.html'

class NegativeSizeList(generic.ListView):
  model = NegativeSize
  template_name = 'schema/list.html'

class OrderList(generic.ListView):
  model = Order
  template_name = 'schema/list.html'

class PaperStockList(generic.ListView):
  model = PaperStock
  template_name = 'schema/list.html'

class PersonList(generic.ListView):
  model = Person
  template_name = 'schema/list.html'

class PrintList(generic.ListView):
  model = Print
  template_name = 'schema/list.html'

class ProcessList(generic.ListView):
  model = Process
  template_name = 'schema/list.html'

class RepairList(generic.ListView):
  model = Repair
  template_name = 'schema/list.html'

class ScanList(generic.ListView):
  model = Scan
  template_name = 'schema/list.html'

class NegativeList(generic.ListView):
  model = Negative
  template_name = 'schema/list.html'

class FilmList(generic.ListView):
  model = Film
  template_name = 'schema/list.html'

class SeriesList(generic.ListView):
  model = Series
  template_name = 'schema/list.html'

class TeleconverterList(generic.ListView):
  model = Teleconverter
  template_name = 'schema/list.html'

class TonerList(generic.ListView):
  model = Toner
  template_name = 'schema/list.html'
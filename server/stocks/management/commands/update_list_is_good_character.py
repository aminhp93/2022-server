from django.core.management.base import BaseCommand

from stocks.models import Stock

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--arg', help="Something helpful")

    def handle(self, *args, **options):
        print(7, args, options)
        self.stdout.write(self.style.SUCCESS('Start update list is_good_character'))

        some_string = "AAAACBACVAGGAGRANVASMBCCBCGBFCBIDBMIBMPBSIBSRBVHBVSBWEC4GCCLCEOCIICKGCRECSVCTDCTGCTICTRCTSD2DDBCDCLDCMDGCDGWDHCDIGDPGDPMDRCDRHDVNDXGELCEVGFCNFPTFRTFTSG36GASGILGMDGTNGVRHAGHAHHAXHBCHCMHDBHDCHDGHHSHIIHPGHPXHSGHT1HTNHUTHVNIDCIDIIDJIJCILBIMPITAKBCKDCKDHKSBLASLCGLHGLPBLSSLTGMBBMBSMIGMPCMSNMSRMWGNHANKGNLGNTCNTLNVLOILPANPC1PETPHRPLCPLXPNJPOMPOWPTBPVCPVDPVPPVSPVTQNSREES99SBTSCRSGPSGTSHBSHSSIPSJSSMCSSISTBSTKSZCTCBTDCTIPTNGTNHTPBTV2TVNVCBVCGVCIVCRVCSVEAVGCVGIVGSVGTVIBVIXVJCVNDVNMVPBVPG"
        # x = 3
        # list_symbols = [some_string[y-x:y] for y in range(x, len(some_string)+x,x)]

        # list_to_update = Stock.objects.filter(symbol__in=list_symbols)
        # Stock.objects.all().update(is_good_character=False)
        # list_to_update.update(is_good_character=True)


        self.stdout.write(self.style.SUCCESS('End update list is_good_character'))

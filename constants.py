"""
constants.py
"""
API_ENCAR_URL = "http://api.encar.com"
INSURANCE_URL = "http://www.encar.com/dc/dc_cardetailview.do?method=kidiFirstPop&carid="
CAR_DETAIL_URL = "http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&carid="
SEARCH_CAR_LIST_URL = "/search/car/list/general"
SEARCH_CAR_LIST_URL_PREMIUM = "/search/car/list/premium"

# SUV 차량이면서, 통풍시트가 있는 차량들
SUV_COOL_SEAT_FILTER = "(And.Hidden.N._.CarType.Y._.Category.SUV._.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_)._.Mileage.range(100000..200000).)"
GRANDEUR_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.그랜저.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
GRANDEUR_WHITE_COOL_SEAT_FILTER = "(And.Hidden.N._.Color.흰색._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.그랜저.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SONATA_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.쏘나타.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
AVANTE_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.아반떼.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
KONA_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.코나.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
TUCSON_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.투싼.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SANTAFE_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.싼타페.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"

K7_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.K7.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
K5_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.K5.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
K3_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.K3.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_)._.FuelType.가솔린+전기.)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
NIRO_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.니로.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SELTOS_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.셀토스.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SPORTAGE_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.스포티지.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SORENTO_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.쏘렌토.))_.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
RAY_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.레이.))_.Condition.Inspection._.Condition.Record.)"
MORNING_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.모닝.))_.Condition.Inspection._.Condition.Record.)"

SM6_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.르노코리아(삼성_)._.ModelGroup.SM6.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_).)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
QM6_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.르노코리아(삼성_)._.ModelGroup.QM6.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_).)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"

CHEVROLET_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.Manufacturer.쉐보레(GM대우_).)_.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
MALIBU_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.쉐보레(GM대우_)._.ModelGroup.말리부.))_.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"

KORANDO_COOL_SEAT_FILTER = "(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.쌍용._.ModelGroup.코란도.))_.Condition.Inspection._.Condition.Record._.(Or.FuelType.가솔린._.FuelType.LPG(일반인 구입_).)_.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"

BIGSIZE_COOL_SEAT_FILTER = "(And.Hidden.N._.CarType.Y._.Category.대형차._.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_)._.Mileage.range(0..200000).)"


LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER = "(And.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_)._.Mileage.range(100000..150000).)"
VERY_LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER = "(And.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_)._.Mileage.range(120000..300000).)"
SHORT_DISTANCE_SUNROOF_COOLSEAT_FILTER = "(And.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_)._.Mileage.range(40000..60000).)"
LPG_COOLSEAT_FILTER = "(And.Mileage.range(0..200000)._.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Condition.Inspection._.Condition.Record._.FuelType.LPG(일반인 구입_)._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
HYBRID_COOLSEAT_FILTER = "(And.Mileage.range(0..200000)._.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Condition.Inspection._.Condition.Record._.FuelType.가솔린+전기._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
HOMESERVICE_COOLSEAT_FILTER = "(And.Mileage.range(30000..200000)._.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Trust.HomeService._.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
FOREIGN_HOMESERVICE_FILTER = "(And.Mileage.range(30000..200000)._.Hidden.N._.CarType.N._.Trust.HomeService._.Condition.Inspection._.Condition.Record._.Options.내비게이션.)"

# 10만 이상 경차, 준중형
SMALL_SIZE_FILTER = "(And.Mileage.range(100000..200000)._.Hidden.N._.CarType.Y._.(Or.Category.경차._.Category.준중형차.)_.Condition.Inspection._.Condition.Record.)"
SMALL_SIZE_LATEST_FILTER = "(And.Mileage.range(40000..60000)._.Hidden.N._.CarType.Y._.(Or.Category.경차._.Category.준중형차.)_.Condition.Inspection._.Condition.Record.)"
SMALL_SIZE_ONLY_FILTER = "(And.Mileage.range(0..200000)._.Hidden.N._.CarType.Y._.Category.경차._.Condition.Inspection._.Condition.Record.)"

RENT_CAR_SUNROOF_FILTER = "(And.Mileage.range(0..200000)._.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Trust.HomeService._.Condition.Inspection._.Condition.Record._.Options.선루프._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
WHITE_CAR_HOMESERVICE_FILTER = "(And.Hidden.N._.CarType.Y._.(Or.Category.준중형차._.Category.중형차._.Category.대형차._.Category.SUV.)_.Trust.HomeService._.Condition.Inspection._.Condition.Record._.Color.흰색._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"

# 오토허브(통풍시틐)
AUTOHUB_COOLSEAT_FILTER = "(And.Hidden.N._.CarType.Y._.DealerShipNm.경기 오토허브._.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"
SUWON_COOLSEAT_FILTER = "(And.Hidden.N._.CarType.Y._.DealerShipNm.경기 도이치오토월드._.Condition.Inspection._.Condition.Record._.Options.통풍시트(운전석_)._.Options.통풍시트(동승석_).)"


# 변경일자 기준, 0 페이지 20개 조회
SEARCH_FILTER = "|ModifiedDate|0|400"

# ENCAR API MAX LIMIT 이 400 이므로 아래와 같이 설정
ENCAR_MAX_LIMIT = 400
$('.popup').on("click", function()
{
    $('.popuptext').removeClass("active");
    $(this).find('.popuptext').addClass("active");
    $('.popup-overlay').addClass("active");
    //tenemos que agregar que abra pestaña Organismo-id
});

$('.popuptext').on("click", function()
{
    $('.popuptext').removeClass("active");
    $('.popup-overlay').removeClass("active");
});

$('.popup-overlay').on("click", function()
{
    $('.popup-overlay').removeClass("active");
    $('.popuptext').removeClass("active");
});
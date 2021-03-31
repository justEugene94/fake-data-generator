jQuery(document).ready(function ($) {
  $('.type-selector').change(function () {
    let selectedOptionText = $(this).children(':selected').text()
    let formNumber = this.id.match(/\d+/)[0]
    let labelSelector = `label[for*=form-${formNumber}-range]`
    let inputRangeMinSelector = `#id_form-${formNumber}-range_min`
    let inputRangeMaxSelector = `#id_form-${formNumber}-range_max`

    if (selectedOptionText === 'Text' || selectedOptionText === 'Integer') {
      $(inputRangeMinSelector).css('visibility', 'visible')
      $(inputRangeMaxSelector).css('visibility', 'visible')
      $(labelSelector).css('visibility', 'visible')
    } else {
      $(inputRangeMinSelector).css('visibility', 'hidden')
      $(inputRangeMaxSelector).css('visibility', 'hidden')
      $(labelSelector).css('visibility', 'hidden')
    }
  })
})
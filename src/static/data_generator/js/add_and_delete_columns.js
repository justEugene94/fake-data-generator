jQuery(document).ready(function () {
  $('[type=button]').click(function (e) {
    let columns = $('.custom-row')
    let formTotalSelector = $('[name=form-TOTAL_FORMS]')
    if ($(this).val() === 'add') {
      let lastColumn = columns.last()
      let clonedLastColumn = lastColumn.clone(true)
      for (let elem of clonedLastColumn) {
        for (let child of elem.children) {
          if (child.tagName === 'LABEL') {
            child.htmlFor = incrementedStringInFormsetElement(child.htmlFor)
          } else if (child.tagName === 'INPUT' || child.tagName === 'SELECT') {
            child.name = incrementedStringInFormsetElement(child.name)
            child.id = incrementedStringInFormsetElement(child.id)
          }
        }
      }
      columns.last().after(clonedLastColumn)
      formTotalSelector.val(parseInt(formTotalSelector.val()) + 1)
    } else {
      if (columns.length > 1) {
        $(this).parent().remove()
        formTotalSelector.val(parseInt(formTotalSelector.val()) - 1)

      }
    }
  })
})

function incrementedStringInFormsetElement (string) {
  let array = string.split('-')
  array[1] = parseInt(array[1]) + 1
  return array.join('-')
}
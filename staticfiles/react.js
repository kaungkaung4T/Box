$('.like-form').submit(function(e){
                e.preventDefault()

                const like = $(this).attr('id')

                const likeText = $(`.like-btn${like}`).text()
                const trim = $.trim(likeText)

                const url = $(this).attr('action')

                let res;
                const likes = $(`.like-count${like}`).text()
                const trimCount = parseInt(likes)

                $.ajax({
                    type: 'POST',
                    url: url,
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                        'like':like,
                    },
                    success: function(response) {
                        if(trim == 'UnReact') {
                            $(`.like-btn${like}`).text('React')
                            res = trimCount - 1
                        } else {
                            $(`.like-btn${like}`).text('UnReact')
                            res = trimCount + 1
                        }

                        $(`.like-count${like}`).text(res)
                    },
                    error: function(response) {
                        console.log('error', response)
                    }
                })

            })
$(document).ready(function() {
    $('#generate-question-btn').click(function() {
        getRandomQuestion();
    });

    $('#generate-helpers-btn').click(function() {
        getQuestionHelpers();
    });
});

function getRandomQuestion() {
        $.get(
            '/get/random/question'
        ).done(function (response) {
            if (response['question']) {
                $('#question-name').text(response['question']);
                $('#question-freq').text(response['ask_freq']);
                $('#question-display').show();
                $('#question-helpers-display').hide();
            } else {
                $('#question-name').text('No questions available.');
                $('#question-display').show();
                $('#question-helpers-display').hide();
            }
            
        }).fail(function (err) {
            alert("error.getQuestion() ended in fail");
        });
}

function getQuestionHelpers() {
    $.get('/get/question/helpers')
        .done(function(response) {
            if (response.helpers && response.helpers.length > 0) {
                $('#question-helpers').empty();
                response.helpers.forEach(function(helper) {
                    $('#question-helpers').append('<li class="list-group-item">' + helper + '</li>');
                });
                $('#question-helpers-display').show();
            } else {
                $('#question-helpers').text('No helpers available.');
                $('#question-helpers-display').show();
            }
        })
        .fail(function(err) {
            alert("Error fetching helpers.");
        });
}
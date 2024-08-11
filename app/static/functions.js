$(document).ready(function() {
    let helpMode = ''; 
    currentSubtopic = ''
    $('#generate-learn-question-btn').click(function() {
        getRandomQuestionToLearn();
        helpMode = 'learn'; 
        $('#generate-helpers-btn').hide();
        $('#generate-subtopics-btn').show();
    });

    $('#generate-answer-question-btn').click(function() {
        getRandomQuestionToAnswer();
        helpMode = 'answer'; 
        $('#generate-subtopics-btn').hide();
        $('#generate-helpers-btn').show();
    });

    $('#generate-subtopics-btn').click(function() {
        getQuestionSubtopics();
    });

    $('#generate-helpers-btn').click(function() {
        getSubtopicHelpers();
    });

    function getRandomQuestionToLearn() {
        $.get('/get/random/questionToLearn')
            .done(function(response) {
                if (response['question']) {
                    $('#question-name').text(response['question']);
                    $('#question-freq').text(response['ask_freq']);
                    $('#question-display').show();
                    $('#question-subtopics-display').hide();
                } else {
                    $('#question-name').text('No questions available.');
                    $('#question-display').show();
                    $('#question-subtopics-display').hide();
                }
            })
            .fail(function(err) {
                alert("error.getRandomQuestionToLearn() ended in fail");
            });
    }

    function getRandomQuestionToAnswer() {
        $.get('/get/random/questionToAnswer')
            .done(function(response) {
                if (response['question']) {
                    $('#question-name').text(response['question']);
                    $('#question-freq').text(response['subtopic']);
                    $('#question-display').show();
                    $('#question-subtopics-display').hide();
                } else {
                    $('#question-name').text('No questions available.');
                    $('#question-display').show();
                    $('#question-subtopics-display').hide();
                }
            })
            .fail(function(err) {
                alert("error.getRandomQuestionToAnswer() ended in fail");
            });
    }

    function getQuestionSubtopics() {
        $.get('/get/question/subtopics')
            .done(function(response) {
                if (response.subtopics && response.subtopics.length > 0) {
                    $('#question-subtopics').empty();
                    response.subtopics.forEach(function(subtopic) {
                        $('#question-subtopics').append(`
                            <li class="list-group-item">
                                ${subtopic}
                                <button id="more-info-btn" class="btn btn-primary" data-subtopic="${subtopic}">
                                    More help
                                </button>
                            </li>
                        `);
                    });
                    $('#question-subtopics-display').show();
                } else {
                    $('#question-subtopics').text('No subtopics available.');
                    $('#question-subtopics-display').show();
                }
            })
            .fail(function(err) {
                alert("Error fetching subtopics.");
            });
    }

    $(document).on('click', '#more-info-btn', function() {
        currentSubtopic = $(this).data('subtopic');
        getSpecificHelpers();
    });

    function getSpecificHelpers() {
        $.get('/get/question/subtopicHelpers', {subtopic: currentSubtopic})
            .done(function(response) {
                if (response.helpers && response.helpers.length > 0) {
                    $('#question-subtopics').empty();
                    response.helpers.forEach(function(helper) {
                        $('#question-subtopics').append('<li class="list-group-item">' + helper + '</li>');
                    });
                    $('#question-subtopics-display').show();
                } else {
                    $('#question-subtopics').text('No helpers available.');
                    $('#question-subtopics-display').show();
                }
            })
            .fail(function(err) {
                alert("Error fetching helpers.");
            });
    }

    function getSubtopicHelpers() {
        $.get('/get/question/helpers')
            .done(function(response) {
                if (response.helpers && response.helpers.length > 0) {
                    $('#question-subtopics').empty();
                    response.helpers.forEach(function(helper) {
                        $('#question-subtopics').append('<li class="list-group-item">' + helper + '</li>');
                    });
                    $('#question-subtopics-display').show();
                } else {
                    $('#question-subtopics').text('No helpers available.');
                    $('#question-subtopics-display').show();
                }
            })
            .fail(function(err) {
                alert("Error fetching helpers.");
            });
    }
});

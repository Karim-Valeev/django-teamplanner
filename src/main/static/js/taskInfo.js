function showTaskInfo(parameters) {
    $('#taskModal .modal-title').html(parameters.title);
    $('#taskModal .description').html(parameters.description);
    $('#taskModal .author').html("@" + parameters.author);
    $('#taskModal .pub_date').html(parameters.pub_date);
    $('#taskModal .lead_time').html("до " + parameters.lead_time);
    $('#taskModal .edit').attr("href", "tasks/edit_task/" + parameters.work_id);
    $('#taskModal .delete').attr("href", "tasks/delete_task/" + parameters.work_id);
    $('#taskModal .comment-form').attr("action", "/tasks/leave_comment/" + parameters.id_for_add_comments);
    $('#taskModal').modal('show');
    if (parameters.is_completed === "True") {
        $('#taskModal .complete-link').attr("href","#").html("Task is completed");
    } else {
        $('#taskModal .complete-link').attr("href", "tasks/complete_task/" + parameters.work_id).html("Mark as completed");
    }
}
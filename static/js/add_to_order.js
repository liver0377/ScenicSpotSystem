$(document).ready(function() {
    $(".add-to-order").click(function(event) {
        event.preventDefault();  // 阻止默认行为，禁止跳转到链接的URL

        var spotId = $(this).data("spot-id");  // 获取景点ID
        var originalUrl = $(this).data("original-url");  // 获取原始URL
        var addTicketUrl = $(this).data("add-ticket-url");

        // 发送 AJAX 请求到 add_ticket_to_order 视图
        $.ajax({
            url: addTicketUrl,
            method: "POST",
            data: {
                spot_id: spotId,
                csrfmiddlewaretoken: csrfToken,
            },
            success: function(response) {
                // 处理成功响应，根据需求进行页面更新或其他操作
                alert("Ticket added to order successfully!");
                
                // 重新加载原始URL或其他操作
                window.location.href = originalUrl;
            },
            error: function(xhr, status, error) {
                // 处理错误响应，根据需求进行错误处理或其他操作
                console.log(error);
            }
        });
    });
});
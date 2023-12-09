import os
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def __get_html_content(self):
        """
        Читаем страницу в формате html
        :return: возврат прочитанный текст
        """
        
        with open(os.path.join('html', 'index.html'), 'r', encoding='utf-8') as file:
            file = file.read()
            return file

    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов
        """

        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":

    # Инициализация веб-сервера, который по заданным параметрам в сети будет
    # принимать запросы и отправлять их на обработку специальному классу, описанному выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
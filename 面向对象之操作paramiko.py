import paramiko
import os

class Handle_paramiko(object):
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        # self.sftp= None

    def do_ssh_client(self, cmd):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        try:
            ssh_client.connect(self.hostname, self.port, self.username, self.password)
        except:
            print("主机%s连接失败，请重新连接" %self.hostname)
        else:
            print("主机%s连接成功" %self.hostname)
            stdin, stdout, stderr = ssh_client.exec_command(cmd)
            res = stdout.read()
            print(res)
            ssh_client.close()

    @staticmethod
    def if_exist_remote_dir(dir):
        try:
            par.sftp.listdir(dir)
        except Exception as err:
            if "No such file" in str(err):
                par.sftp.mkdir(dir)

    def sftp_client(self):
        trans = paramiko.Transport(self.hostname, self.port)
        try:
            # print(self.username, self.password)
            trans.connect(username=self.username, password=self.password)
            # trans.connect(username='zhang', password='123456')
        except:
            print("主机%s连接失败，请重新连接" %self.hostname)
        else:
            sftp = paramiko.SFTPClient.from_transport(trans)
            print("sftp客户端创建成功")
            self.sftp = sftp

    def do_upload(self, local_path, remote_path):
        file_dir = "/".join(remote_path.split("/")[:-1])
        print(file_dir)
        self.if_exist_remote_dir(file_dir)
        if not os.path.exists(local_path):
            print("该文件不存在，请上传已存在的文件")
        else:
            self.sftp.put(local_path, remote_path)
            print("本地文件%s成功上传到%s服务器" % (local_path, self.hostname), )
            # print("本地文件%s成功上传到%s服务器", self.hostname)
            self.sftp.close()

    def do_download(self, remote_path, download_path):
        remote_dir = '/'.join(remote_path.split("/")[:-1])
        print(remote_dir)
        remote_filename = remote_path.split("/")[-1]
        print(remote_path)
        if remote_filename not in self.sftp.listdir(remote_dir):
            print("该文件不存在，请下载已存在的文件")
        # elif not self.sftp.listdir():
        #     print("提示: 请输入正确的下载路径!")
        else:
            self.sftp.get(remote_path, download_path)
            print("服务器%s的文件%s成功下载到本地"%(self.hostname, download_path))

    def sftp_close(self, trans):
        trans.close()
        print('两台主机建立的通道关闭')


if __name__ == '__main__':
    par = Handle_paramiko("192.168.43.234", 22, "root", "123456")
    cmd = "python git_test.py"
    # par.do_ssh_client(cmd)
    par.sftp_client()
    # res = par.do_upload("面向对象之操作MySQL.py", "/home/liu/面向对象之操作MySQL.py")
    # print(res)

    par.do_download("/home/zhang/zhang.txt", "zhang.txt")

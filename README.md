# FZUNetworkAutoConnect 

本项目用于自动连接福州大学教学区校园网  
检测网络状态是否正常,若有问题则自动重连  

## 依赖

```
python 3
requests
```

## 使用方法

将项目clone至本地  

```shell
git clone https://github.com/Dark-Existed/FZUNetworkAutoConnect.git  
```

在 **connect_network.py** 中, 填入账号信息    
```python
username = ''
password = ''
```

在**Linux**下可使用**crontab**,定时执行  
如每三小时执行一次  
```shell
0 */3 * * * python3 <file path>
```

---

This project is for auto connect the network in the teaching area of FZU.  
Check whether the network status is normal, and automatically reconnect if there is a problem.

## Dependencies

```
python 3
requests
```

## Usage  
Clone the project to local

```shell
git clone https://github.com/Dark-Existed/FZUNetworkAutoConnect.git  
```
Fill you account in **connect_network.py**    

```python
username = ''
password = ''
```
On Linux can ues **crontab** to execute regularly.  
Such as every three hours.

```shell
0 */3 * * * python3 <file path>
```
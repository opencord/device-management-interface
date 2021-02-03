# Examples of usage of the APIs

BBSim implements the Device Management Interface and most of the examples of usage of the APIs using grpurl can be found in the [BBSim docs here](https://github.com/opencord/bbsim/blob/master/docs/source/DMI_Server_README.md)

## Image Management APIs

### DownloadImage

```sh
$ grpcurl -v -plaintext -d "{\"device_uuid\": {\"uuid\": \"$UUID\"}, \"image_info\": {\"image_url\": \"sftp://$USER:$PASSWORD@10.34.90.43:22/upload/olt-image-v1.2.3-onie_inst.bin\"}}" $DM_IP dmi.NativeSoftwareManagementService.DownloadImage
```

### ActivateImage

``` sh
$ grpcurl -v -plaintext -d "{\"uuid\": {\"uuid\": \"$UUID\"}}" $DM_IP dmi.NativeSoftwareManagementService.ActivateImage
```

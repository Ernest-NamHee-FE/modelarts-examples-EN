{"model_type":"TensorFlow",
# Model precision information, including F1, accuracy, precision, and recall rate. The training mnist is unnecessary and can be set randomly. 
"metrics":{"f1":0.61185,"accuracy":0.8361458991671805,"precision":0.4775016224869111,"recall":0.8513980485387226},
# Dependency package "dependencies":
[{"installer":"pip","packages":[{"restraint":"ATLEAST","package_version":"1.15.0","package_name":"numpy"},{"restraint":"","package_version":"","package_name":"h5py"},{"restraint":"ATLEAST","package_version":"1.8.0","package_name":"tensorflow"},{"restraint":"ATLEAST","package_version":"5.2.0","package_name":"Pillow"}]}] required for reasoning,
# Model algorithm type. Here, it is the image classification model "model_algorithm":"image_classification","apis":
[{"procotol": "HYPERLINK "https://www.json.cn/http" \t "_blank" http","url":"/","request":{"Content-type":"multipart/form-data","data":{"type":"object","properties":{"images":{"type":"file"}}}},"method":"post","response":{"Content-type":"multipart/form-data","data":{"required":["predicted_label","scores"],"type":"object","properties":{"predicted_label":{"type":"string"},"scores":{"items":{"minItems":2,"items":[{"type":"string"},{"type":"number"}],"type":"array","maxItems":2},"type":"array"}}}}}]
  }

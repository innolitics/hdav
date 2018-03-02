# High Dimensional Algorithm Viewer (HDAV)

Hdav is a python library that facilitates viewing 2- and 3-D multi-layered image data.

## Example Use Case

```python
import hdav
hdav.view(layers=[
    {
        'name': 'CT',
        'data': ct_voxels_preop,
        'visible': True,
    },
    {
        'name': 'MRI',
        'data': mri_voxels_preop,
        'visible': True
    }
], interactive=True, window_id='pre operative')
hdav.view(layers=[
    {
        'name': 'CT',
        'data': ct_voxels_postop,
        'visible': True,
    },
    {
        'name': 'MRI',
        'data': mri_voxels_postop,
        'visible': True
    }
], interactive=True, window_id='post operative')
```

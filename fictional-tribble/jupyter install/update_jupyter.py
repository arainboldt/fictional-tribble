"""
Script to update jupyter notebooks

"""
import os
import shutil
import site

def main():
    print('!!Warning!! This will delete any work saved in standard notebooks')
    jupyter_notebooks = 'Jupyter_Notebooks'
    desktop = os.path.join(os.environ["HOMEPATH"], 'Desktop')
    assert os.path.isdir(desktop)
    os.makedirs(os.path.join(desktop, jupyter_notebooks), exist_ok=True)
    fictional_tribble_notebooks = None
    for site_packages in site.getsitepackages():
        if 'fictional-tribble' in os.listdir(site_packages):
            fictional_tribble_notebooks = os.path.join(site_packages, 'fictional-tribble', 'Notebooks')
            break
    if fictional_tribble_notebooks is None:
        raise OSError('Jupyter Learning Environment Not Installed')
    for notebook in os.listdir(fictional_tribble_notebooks):
        if os.path.isfile(notebook) and ('ipynb' in notebook.split('.', 1)[1]):
            if os.path.isfile(os.path.join(desktop, jupyter_notebooks, notebook)):
                os.remove(os.path.join(desktop, jupyter_notebooks, notebook))
            shutil.copy(os.path.join(fictional_tribble_notebooks, notebook),
                        os.path.join(desktop, jupyter_notebooks, notebook ))

if __name__ == '__main__':
    main()
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponseRedirect
from upload_app.forms import UploadFileForm

def handle_uploaded_file(f):
    # Read the file using pandas
    if f.name.endswith('.csv'):
        df = pd.read_csv(f)
    elif f.name.endswith('.xls') or f.name.endswith('.xlsx'):
        df = pd.read_excel(f)
    else:
        return None

    # Generate a summary report
    summary = df.to_html()
    print("hhh-->",summary)
    return summary

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            return render(request, 'uploader/summary.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'uploader/upload.html', {'form': form})

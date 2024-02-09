from google.cloud import storage
import os

def upload_files_to_gcs(bucket_name, source_folder):
    """Faz o upload de arquivos de um diretório local para o GCS.

    Parâmetros:
    bucket_name (str): Nome do bucket do GCS.
    source_folder (str): Caminho do diretório local contendo os arquivos a serem carregados.
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Lista todos os arquivos no diretório local
    for filename in os.listdir(source_folder):
        local_path = os.path.join(source_folder, filename)

        # Certifique-se de que é um arquivo e não um diretório
        if os.path.isfile(local_path):
            # Define o caminho no GCS (pode incluir subdiretórios)
            blob = bucket.blob(filename)

            # Faz o upload do arquivo para o GCS
            blob.upload_from_filename(local_path)
            print(f"{filename} carregado para o bucket {bucket_name}.")

# Substitua 'seu-bucket' pelo nome do seu bucket no GCS
# Substitua './datasets' pelo caminho do seu diretório local, se necessário
upload_files_to_gcs('de-zoomcamp-green-taxi-data-giuseppe', './datasets')

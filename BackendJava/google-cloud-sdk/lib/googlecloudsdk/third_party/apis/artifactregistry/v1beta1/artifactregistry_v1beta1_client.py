"""Generated client library for artifactregistry version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.artifactregistry.v1beta1 import artifactregistry_v1beta1_messages as messages


class ArtifactregistryV1beta1(base_api.BaseApiClient):
  """Generated client library for service artifactregistry version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://artifactregistry.googleapis.com/'
  MTLS_BASE_URL = 'https://artifactregistry.mtls.googleapis.com/'

  _PACKAGE = 'artifactregistry'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ArtifactregistryV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new artifactregistry handle."""
    url = url or self.BASE_URL
    super(ArtifactregistryV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_repositories_files = self.ProjectsLocationsRepositoriesFilesService(self)
    self.projects_locations_repositories_packages_tags = self.ProjectsLocationsRepositoriesPackagesTagsService(self)
    self.projects_locations_repositories_packages_versions = self.ProjectsLocationsRepositoriesPackagesVersionsService(self)
    self.projects_locations_repositories_packages = self.ProjectsLocationsRepositoriesPackagesService(self)
    self.projects_locations_repositories = self.ProjectsLocationsRepositoriesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (ArtifactregistryProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesFilesService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_files resource."""

    _NAME = 'projects_locations_repositories_files'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsRepositoriesFilesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets a file.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesFilesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (File) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/files/{filesId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.files.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesFilesGetRequest',
        response_type_name='File',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists files.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesFilesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListFilesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/files',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.files.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/files',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesFilesListRequest',
        response_type_name='ListFilesResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesPackagesTagsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_packages_tags resource."""

    _NAME = 'projects_locations_repositories_packages_tags'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsRepositoriesPackagesTagsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a tag.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesTagsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Tag) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/tags',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.packages.tags.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['tagId'],
        relative_path='v1beta1/{+parent}/tags',
        request_field='tag',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesTagsCreateRequest',
        response_type_name='Tag',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a tag.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesTagsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/tags/{tagsId}',
        http_method='DELETE',
        method_id='artifactregistry.projects.locations.repositories.packages.tags.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesTagsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a tag.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesTagsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Tag) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/tags/{tagsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.tags.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesTagsGetRequest',
        response_type_name='Tag',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists tags.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesTagsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTagsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/tags',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.tags.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/tags',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesTagsListRequest',
        response_type_name='ListTagsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a tag.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesTagsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Tag) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/tags/{tagsId}',
        http_method='PATCH',
        method_id='artifactregistry.projects.locations.repositories.packages.tags.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='tag',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesTagsPatchRequest',
        response_type_name='Tag',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesPackagesVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_packages_versions resource."""

    _NAME = 'projects_locations_repositories_packages_versions'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsRepositoriesPackagesVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a version and all of its content. The returned operation will complete once the version has been deleted.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/versions/{versionsId}',
        http_method='DELETE',
        method_id='artifactregistry.projects.locations.repositories.packages.versions.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force'],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a version.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Version) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/versions/{versionsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.versions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsGetRequest',
        response_type_name='Version',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists versions.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}/versions',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.versions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['orderBy', 'pageSize', 'pageToken', 'view'],
        relative_path='v1beta1/{+parent}/versions',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesVersionsListRequest',
        response_type_name='ListVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesPackagesService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories_packages resource."""

    _NAME = 'projects_locations_repositories_packages'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsRepositoriesPackagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a package and all of its versions and tags. The returned operation will complete once the package has been deleted.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}',
        http_method='DELETE',
        method_id='artifactregistry.projects.locations.repositories.packages.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a package.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Package) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages/{packagesId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesGetRequest',
        response_type_name='Package',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists packages.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPackagesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPackagesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}/packages',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.packages.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/packages',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPackagesListRequest',
        response_type_name='ListPackagesResponse',
        supports_download=False,
    )

  class ProjectsLocationsRepositoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_repositories resource."""

    _NAME = 'projects_locations_repositories'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsRepositoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['repositoryId'],
        relative_path='v1beta1/{+parent}/repositories',
        request_field='repository',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='DELETE',
        method_id='artifactregistry.projects.locations.repositories.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Repository) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesGetRequest',
        response_type_name='Repository',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the IAM policy for a given resource.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}:getIamPolicy',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists repositories.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRepositoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories',
        http_method='GET',
        method_id='artifactregistry.projects.locations.repositories.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/repositories',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesListRequest',
        response_type_name='ListRepositoriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a repository.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Repository) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}',
        http_method='PATCH',
        method_id='artifactregistry.projects.locations.repositories.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='repository',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesPatchRequest',
        response_type_name='Repository',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Updates the IAM policy for a given resource.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}:setIamPolicy',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Tests if the caller has a list of permissions on a resource.

      Args:
        request: (ArtifactregistryProjectsLocationsRepositoriesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/repositories/{repositoriesId}:testIamPermissions',
        http_method='POST',
        method_id='artifactregistry.projects.locations.repositories.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='ArtifactregistryProjectsLocationsRepositoriesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (ArtifactregistryProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='artifactregistry.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (ArtifactregistryProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='artifactregistry.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/locations',
        request_field='',
        request_type_name='ArtifactregistryProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ArtifactregistryV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
